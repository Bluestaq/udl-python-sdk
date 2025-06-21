# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SensorGetResponse,
    SensorListResponse,
    SensorTupleResponse,
    SensorQueryhelpResponse,
)
from unifieddatalibrary._utils import parse_date, parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSensor:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        sensor = client.sensor.create(
            classification_marking="U",
            data_mode="TEST",
            sensor_name="SENSOR_NAME",
            source="some.user",
        )
        assert sensor is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        sensor = client.sensor.create(
            classification_marking="U",
            data_mode="TEST",
            sensor_name="SENSOR_NAME",
            source="some.user",
            active=True,
            af_id="AF-ID",
            asr_type="SENSOR_TYPE",
            data_control="observations",
            entity={
                "classification_marking": "U",
                "data_mode": "TEST",
                "name": "Example name",
                "source": "Bluestaq",
                "type": "ONORBIT",
                "country_code": "US",
                "id_entity": "ENTITY-ID",
                "id_location": "LOCATION-ID",
                "id_on_orbit": "ONORBIT-ID",
                "id_operating_unit": "OPERATINGUNIT-ID",
                "location": {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "name": "Example location",
                    "source": "Bluestaq",
                    "altitude": 10.23,
                    "country_code": "US",
                    "id_location": "LOCATION-ID",
                    "lat": 45.23,
                    "lon": 179.1,
                    "origin": "THIRD_PARTY_DATASOURCE",
                },
                "on_orbit": {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "sat_no": 1,
                    "source": "Bluestaq",
                    "alt_name": "Alternate Name",
                    "category": "Lunar",
                    "common_name": "Example common name",
                    "constellation": "Big Dipper",
                    "country_code": "US",
                    "decay_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "id_on_orbit": "ONORBIT-ID",
                    "intl_des": "2021123ABC",
                    "launch_date": parse_date("2018-01-01"),
                    "launch_site_id": "LAUNCHSITE-ID",
                    "lifetime_years": 10,
                    "mission_number": "Expedition 1",
                    "object_type": "PAYLOAD",
                    "origin": "THIRD_PARTY_DATASOURCE",
                },
                "origin": "THIRD_PARTY_DATASOURCE",
                "owner_type": "Commercial",
                "taskable": False,
                "terrestrial_id": "TERRESTRIAL-ID",
                "urls": ["URL1", "URL2"],
            },
            id_entity="ENTITY-ID",
            id_sensor="SENSOR-ID",
            origin="THIRD_PARTY_DATASOURCE",
            sensorcharacteristics=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sensor": "SENSOR-ID",
                    "source": "Bluestaq",
                    "id": "SENSORCHARACTERISTICS-ID",
                    "accept_sample_ranges": [3.01, 3.02],
                    "analog_to_digital_bit_size": 2,
                    "aperture": 2.23,
                    "asr_scan_rate": 20.23,
                    "atmos_receiver_loss": 0.5,
                    "atmos_transmission_loss": 0.5,
                    "avg_atmos_seeing_conditions": 10.23,
                    "az_angs": [135.1, 45.2],
                    "azimuth_rate": 0.3334,
                    "background_sky_radiance": 10.23,
                    "background_sky_vis_mag": 10.23,
                    "band": "BAND",
                    "bandwidth": 100.23,
                    "beam_order": ["vb1", "ob1"],
                    "beam_qty": 2,
                    "boresight": 20.23,
                    "boresight_off_angle": 20.23,
                    "center_wavelength": 4.56,
                    "collapsing_loss": 1.23,
                    "crit_shear": 47.1,
                    "dark_current": 12.3,
                    "delay_gates": [690.2, 690.3],
                    "description": "PROFILER DATA - PROFILE/SOUNDER DATA FROM PRIMARY WINDS SOURCE",
                    "detect_snr": 2.1,
                    "duty_cycle": 0.5,
                    "earth_limb_excl_hgt": 20.23,
                    "el_angs": [75.3, 75.4],
                    "elevation_rate_geolm": 0.9555,
                    "equipment_type": "PS",
                    "fan_beam_width": 3.1,
                    "fft": 4096,
                    "fgp_crit": 5,
                    "filter_mismatch_factor": 10.23,
                    "f_num": 1.23,
                    "focal_point": 20.23,
                    "h_fov": 20.23,
                    "h_res_pixels": 1000,
                    "k": 1.4,
                    "left_clock_angle": 20.23,
                    "left_geo_belt_limit": 20.23,
                    "location": "KENNEDY SPACE CENTER, FL",
                    "loop_gain": 150.1,
                    "lunar_excl_angle": 45.2,
                    "mag_dec": 45.23,
                    "magnitude_limit": 23.5,
                    "max_deviation_angle": 20.23,
                    "max_integration_time": 1.1,
                    "max_observable_range": 20.23,
                    "max_range_limit": 4972.1,
                    "max_wavelength": 7.89,
                    "min_integration_time": 0.3,
                    "min_range_limit": 165.1,
                    "min_signal_noise_ratio": 31.5,
                    "min_wavelength": 1.23,
                    "negative_range_rate_limit": -19.25,
                    "noise_figure": 10.23,
                    "non_coherent_integrated_pulses": 2,
                    "num_integrated_pulses": 10,
                    "num_integration_frames": 2,
                    "num_optical_integration_modes": 2,
                    "num_waveforms": 2,
                    "optical_integration_angular_rates": [15.1, 0.1],
                    "optical_integration_frames": [2.1, 3.1],
                    "optical_integration_pixel_binnings": [2.1, 1.1],
                    "optical_integration_sn_rs": [6.1, 6.1],
                    "optical_integration_times": [0.3, 1],
                    "optical_transmission": 0.5,
                    "pattern_absorption_loss": 1.23,
                    "pattern_scan_loss": 1.23,
                    "peak_power": 5000000.1,
                    "pixel_instantaneous_fov": 10.23,
                    "pixel_well_depth": 12,
                    "positive_range_rate_limit": 19.25,
                    "prf": 20.23,
                    "prob_detect_snr": 0.5,
                    "prob_false_alarm": 0.5,
                    "pulse_rep_periods": [153.8, 153.9],
                    "quantum_eff": 0.5,
                    "radar_frequency": 45300000000.1,
                    "radar_message_format": "DATA_FORMAT",
                    "radar_mur": 20.23,
                    "radar_pulse_widths": [20.23, 20.33],
                    "radio_frequency": 20.23,
                    "radome_loss": 1.23,
                    "range_gates": [51, 52],
                    "range_spacings": [690.2, 690.3],
                    "read_noise": 12,
                    "receive_gain": 10.2,
                    "receive_horiz_beam_width": 75.3,
                    "receive_loss": 1.23,
                    "receive_vert_beam_width": 75.4,
                    "ref_temp": 3.5,
                    "req_records": [0, 1],
                    "right_clock_angle": 20.23,
                    "right_geo_belt_limit": 20.23,
                    "run_mean_codes": [0, 5],
                    "signal_processing_loss": 1.23,
                    "site_code": "07",
                    "solar_excl_angle": 50.5,
                    "spec_avg_spectra_nums": [3, 4],
                    "system_noise_temperature": 3.5,
                    "taskable_range": 20.23,
                    "temp_med_filt_codes": [3, 4],
                    "test_number": "02022",
                    "tot_rec_nums": [5, 2],
                    "tower_height": 20.23,
                    "track_angle": 0.043,
                    "track_snr": 15.1,
                    "transmit_gain": 32.1,
                    "transmit_horiz_beam_width": 135.1,
                    "transmit_loss": 7.1,
                    "transmit_power": 190000.1,
                    "transmit_vert_beam_width": 45.2,
                    "true_north_corrector": 10,
                    "true_tilt": 20.23,
                    "twilight_angle": 7.5,
                    "vert_beam_flag": False,
                    "vert_gate_spacings": [149.1, 149.2],
                    "vert_gate_widths": [149.1, 149.2],
                    "v_fov": 20.23,
                    "v_res_pixels": 1000,
                    "waveform_bandwidths": [0.25, 0.25],
                    "waveform_loop_gains": [150.1, 155.1],
                    "waveform_max_ranges": [2000.1, 2000.1],
                    "waveform_min_ranges": [150.1, 150.1],
                    "waveform_pulse_widths": [100.1, 200.1],
                    "z1_max_range": 50.23,
                    "z1_min_range": 20.23,
                    "z2_max_range": 50.23,
                    "z2_min_range": 20.23,
                }
            ],
            sensorlimits_collection=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "id_sensor": "SENSORLIMITS-ID",
                    "id_sensor_limits": "SENSORLIMITS-ID",
                    "lower_left_azimuth_limit": 1.23,
                    "lower_left_elevation_limit": 1.23,
                    "lower_right_azimuth_limit": 1.23,
                    "lower_right_elevation_limit": 1.23,
                    "upper_left_azimuth_limit": 1.23,
                    "upper_left_elevation_limit": 1.23,
                    "upper_right_azimuth_limit": 1.23,
                    "upper_right_elevation_limit": 1.23,
                }
            ],
            sensor_number=1234,
            sensor_observation_type={
                "id": "3",
                "type": "5",
            },
            sensor_stats=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sensor": "idSensor",
                    "source": "Bluestaq",
                    "id": "SENSORSTATS-ID",
                    "last_ob_time": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
            sensor_type={
                "id": 12344411,
                "type": "Space Borne",
            },
            short_name="SNR-1",
        )
        assert sensor is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.sensor.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            sensor_name="SENSOR_NAME",
            source="some.user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = response.parse()
        assert sensor is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.sensor.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            sensor_name="SENSOR_NAME",
            source="some.user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = response.parse()
            assert sensor is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        sensor = client.sensor.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            sensor_name="SENSOR_NAME",
            source="some.user",
        )
        assert sensor is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        sensor = client.sensor.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            sensor_name="SENSOR_NAME",
            source="some.user",
            active=True,
            af_id="AF-ID",
            asr_type="SENSOR_TYPE",
            data_control="observations",
            entity={
                "classification_marking": "U",
                "data_mode": "TEST",
                "name": "Example name",
                "source": "Bluestaq",
                "type": "ONORBIT",
                "country_code": "US",
                "id_entity": "ENTITY-ID",
                "id_location": "LOCATION-ID",
                "id_on_orbit": "ONORBIT-ID",
                "id_operating_unit": "OPERATINGUNIT-ID",
                "location": {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "name": "Example location",
                    "source": "Bluestaq",
                    "altitude": 10.23,
                    "country_code": "US",
                    "id_location": "LOCATION-ID",
                    "lat": 45.23,
                    "lon": 179.1,
                    "origin": "THIRD_PARTY_DATASOURCE",
                },
                "on_orbit": {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "sat_no": 1,
                    "source": "Bluestaq",
                    "alt_name": "Alternate Name",
                    "category": "Lunar",
                    "common_name": "Example common name",
                    "constellation": "Big Dipper",
                    "country_code": "US",
                    "decay_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "id_on_orbit": "ONORBIT-ID",
                    "intl_des": "2021123ABC",
                    "launch_date": parse_date("2018-01-01"),
                    "launch_site_id": "LAUNCHSITE-ID",
                    "lifetime_years": 10,
                    "mission_number": "Expedition 1",
                    "object_type": "PAYLOAD",
                    "origin": "THIRD_PARTY_DATASOURCE",
                },
                "origin": "THIRD_PARTY_DATASOURCE",
                "owner_type": "Commercial",
                "taskable": False,
                "terrestrial_id": "TERRESTRIAL-ID",
                "urls": ["URL1", "URL2"],
            },
            id_entity="ENTITY-ID",
            id_sensor="SENSOR-ID",
            origin="THIRD_PARTY_DATASOURCE",
            sensorcharacteristics=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sensor": "SENSOR-ID",
                    "source": "Bluestaq",
                    "id": "SENSORCHARACTERISTICS-ID",
                    "accept_sample_ranges": [3.01, 3.02],
                    "analog_to_digital_bit_size": 2,
                    "aperture": 2.23,
                    "asr_scan_rate": 20.23,
                    "atmos_receiver_loss": 0.5,
                    "atmos_transmission_loss": 0.5,
                    "avg_atmos_seeing_conditions": 10.23,
                    "az_angs": [135.1, 45.2],
                    "azimuth_rate": 0.3334,
                    "background_sky_radiance": 10.23,
                    "background_sky_vis_mag": 10.23,
                    "band": "BAND",
                    "bandwidth": 100.23,
                    "beam_order": ["vb1", "ob1"],
                    "beam_qty": 2,
                    "boresight": 20.23,
                    "boresight_off_angle": 20.23,
                    "center_wavelength": 4.56,
                    "collapsing_loss": 1.23,
                    "crit_shear": 47.1,
                    "dark_current": 12.3,
                    "delay_gates": [690.2, 690.3],
                    "description": "PROFILER DATA - PROFILE/SOUNDER DATA FROM PRIMARY WINDS SOURCE",
                    "detect_snr": 2.1,
                    "duty_cycle": 0.5,
                    "earth_limb_excl_hgt": 20.23,
                    "el_angs": [75.3, 75.4],
                    "elevation_rate_geolm": 0.9555,
                    "equipment_type": "PS",
                    "fan_beam_width": 3.1,
                    "fft": 4096,
                    "fgp_crit": 5,
                    "filter_mismatch_factor": 10.23,
                    "f_num": 1.23,
                    "focal_point": 20.23,
                    "h_fov": 20.23,
                    "h_res_pixels": 1000,
                    "k": 1.4,
                    "left_clock_angle": 20.23,
                    "left_geo_belt_limit": 20.23,
                    "location": "KENNEDY SPACE CENTER, FL",
                    "loop_gain": 150.1,
                    "lunar_excl_angle": 45.2,
                    "mag_dec": 45.23,
                    "magnitude_limit": 23.5,
                    "max_deviation_angle": 20.23,
                    "max_integration_time": 1.1,
                    "max_observable_range": 20.23,
                    "max_range_limit": 4972.1,
                    "max_wavelength": 7.89,
                    "min_integration_time": 0.3,
                    "min_range_limit": 165.1,
                    "min_signal_noise_ratio": 31.5,
                    "min_wavelength": 1.23,
                    "negative_range_rate_limit": -19.25,
                    "noise_figure": 10.23,
                    "non_coherent_integrated_pulses": 2,
                    "num_integrated_pulses": 10,
                    "num_integration_frames": 2,
                    "num_optical_integration_modes": 2,
                    "num_waveforms": 2,
                    "optical_integration_angular_rates": [15.1, 0.1],
                    "optical_integration_frames": [2.1, 3.1],
                    "optical_integration_pixel_binnings": [2.1, 1.1],
                    "optical_integration_sn_rs": [6.1, 6.1],
                    "optical_integration_times": [0.3, 1],
                    "optical_transmission": 0.5,
                    "pattern_absorption_loss": 1.23,
                    "pattern_scan_loss": 1.23,
                    "peak_power": 5000000.1,
                    "pixel_instantaneous_fov": 10.23,
                    "pixel_well_depth": 12,
                    "positive_range_rate_limit": 19.25,
                    "prf": 20.23,
                    "prob_detect_snr": 0.5,
                    "prob_false_alarm": 0.5,
                    "pulse_rep_periods": [153.8, 153.9],
                    "quantum_eff": 0.5,
                    "radar_frequency": 45300000000.1,
                    "radar_message_format": "DATA_FORMAT",
                    "radar_mur": 20.23,
                    "radar_pulse_widths": [20.23, 20.33],
                    "radio_frequency": 20.23,
                    "radome_loss": 1.23,
                    "range_gates": [51, 52],
                    "range_spacings": [690.2, 690.3],
                    "read_noise": 12,
                    "receive_gain": 10.2,
                    "receive_horiz_beam_width": 75.3,
                    "receive_loss": 1.23,
                    "receive_vert_beam_width": 75.4,
                    "ref_temp": 3.5,
                    "req_records": [0, 1],
                    "right_clock_angle": 20.23,
                    "right_geo_belt_limit": 20.23,
                    "run_mean_codes": [0, 5],
                    "signal_processing_loss": 1.23,
                    "site_code": "07",
                    "solar_excl_angle": 50.5,
                    "spec_avg_spectra_nums": [3, 4],
                    "system_noise_temperature": 3.5,
                    "taskable_range": 20.23,
                    "temp_med_filt_codes": [3, 4],
                    "test_number": "02022",
                    "tot_rec_nums": [5, 2],
                    "tower_height": 20.23,
                    "track_angle": 0.043,
                    "track_snr": 15.1,
                    "transmit_gain": 32.1,
                    "transmit_horiz_beam_width": 135.1,
                    "transmit_loss": 7.1,
                    "transmit_power": 190000.1,
                    "transmit_vert_beam_width": 45.2,
                    "true_north_corrector": 10,
                    "true_tilt": 20.23,
                    "twilight_angle": 7.5,
                    "vert_beam_flag": False,
                    "vert_gate_spacings": [149.1, 149.2],
                    "vert_gate_widths": [149.1, 149.2],
                    "v_fov": 20.23,
                    "v_res_pixels": 1000,
                    "waveform_bandwidths": [0.25, 0.25],
                    "waveform_loop_gains": [150.1, 155.1],
                    "waveform_max_ranges": [2000.1, 2000.1],
                    "waveform_min_ranges": [150.1, 150.1],
                    "waveform_pulse_widths": [100.1, 200.1],
                    "z1_max_range": 50.23,
                    "z1_min_range": 20.23,
                    "z2_max_range": 50.23,
                    "z2_min_range": 20.23,
                }
            ],
            sensorlimits_collection=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "id_sensor": "SENSORLIMITS-ID",
                    "id_sensor_limits": "SENSORLIMITS-ID",
                    "lower_left_azimuth_limit": 1.23,
                    "lower_left_elevation_limit": 1.23,
                    "lower_right_azimuth_limit": 1.23,
                    "lower_right_elevation_limit": 1.23,
                    "upper_left_azimuth_limit": 1.23,
                    "upper_left_elevation_limit": 1.23,
                    "upper_right_azimuth_limit": 1.23,
                    "upper_right_elevation_limit": 1.23,
                }
            ],
            sensor_number=1234,
            sensor_observation_type={
                "id": "3",
                "type": "5",
            },
            sensor_stats=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sensor": "idSensor",
                    "source": "Bluestaq",
                    "id": "SENSORSTATS-ID",
                    "last_ob_time": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
            sensor_type={
                "id": 12344411,
                "type": "Space Borne",
            },
            short_name="SNR-1",
        )
        assert sensor is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.sensor.with_raw_response.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            sensor_name="SENSOR_NAME",
            source="some.user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = response.parse()
        assert sensor is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.sensor.with_streaming_response.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            sensor_name="SENSOR_NAME",
            source="some.user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = response.parse()
            assert sensor is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sensor.with_raw_response.update(
                id="",
                classification_marking="U",
                data_mode="TEST",
                sensor_name="SENSOR_NAME",
                source="some.user",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        sensor = client.sensor.list()
        assert_matches_type(SyncOffsetPage[SensorListResponse], sensor, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        sensor = client.sensor.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[SensorListResponse], sensor, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.sensor.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = response.parse()
        assert_matches_type(SyncOffsetPage[SensorListResponse], sensor, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.sensor.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = response.parse()
            assert_matches_type(SyncOffsetPage[SensorListResponse], sensor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        sensor = client.sensor.delete(
            "id",
        )
        assert sensor is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.sensor.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = response.parse()
        assert sensor is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.sensor.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = response.parse()
            assert sensor is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sensor.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        sensor = client.sensor.count()
        assert_matches_type(str, sensor, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        sensor = client.sensor.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, sensor, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.sensor.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = response.parse()
        assert_matches_type(str, sensor, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.sensor.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = response.parse()
            assert_matches_type(str, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        sensor = client.sensor.get(
            id="id",
        )
        assert_matches_type(SensorGetResponse, sensor, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        sensor = client.sensor.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SensorGetResponse, sensor, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.sensor.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = response.parse()
        assert_matches_type(SensorGetResponse, sensor, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.sensor.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = response.parse()
            assert_matches_type(SensorGetResponse, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sensor.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        sensor = client.sensor.queryhelp()
        assert_matches_type(SensorQueryhelpResponse, sensor, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.sensor.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = response.parse()
        assert_matches_type(SensorQueryhelpResponse, sensor, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.sensor.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = response.parse()
            assert_matches_type(SensorQueryhelpResponse, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        sensor = client.sensor.tuple(
            columns="columns",
        )
        assert_matches_type(SensorTupleResponse, sensor, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        sensor = client.sensor.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SensorTupleResponse, sensor, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.sensor.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = response.parse()
        assert_matches_type(SensorTupleResponse, sensor, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.sensor.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = response.parse()
            assert_matches_type(SensorTupleResponse, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSensor:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor = await async_client.sensor.create(
            classification_marking="U",
            data_mode="TEST",
            sensor_name="SENSOR_NAME",
            source="some.user",
        )
        assert sensor is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor = await async_client.sensor.create(
            classification_marking="U",
            data_mode="TEST",
            sensor_name="SENSOR_NAME",
            source="some.user",
            active=True,
            af_id="AF-ID",
            asr_type="SENSOR_TYPE",
            data_control="observations",
            entity={
                "classification_marking": "U",
                "data_mode": "TEST",
                "name": "Example name",
                "source": "Bluestaq",
                "type": "ONORBIT",
                "country_code": "US",
                "id_entity": "ENTITY-ID",
                "id_location": "LOCATION-ID",
                "id_on_orbit": "ONORBIT-ID",
                "id_operating_unit": "OPERATINGUNIT-ID",
                "location": {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "name": "Example location",
                    "source": "Bluestaq",
                    "altitude": 10.23,
                    "country_code": "US",
                    "id_location": "LOCATION-ID",
                    "lat": 45.23,
                    "lon": 179.1,
                    "origin": "THIRD_PARTY_DATASOURCE",
                },
                "on_orbit": {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "sat_no": 1,
                    "source": "Bluestaq",
                    "alt_name": "Alternate Name",
                    "category": "Lunar",
                    "common_name": "Example common name",
                    "constellation": "Big Dipper",
                    "country_code": "US",
                    "decay_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "id_on_orbit": "ONORBIT-ID",
                    "intl_des": "2021123ABC",
                    "launch_date": parse_date("2018-01-01"),
                    "launch_site_id": "LAUNCHSITE-ID",
                    "lifetime_years": 10,
                    "mission_number": "Expedition 1",
                    "object_type": "PAYLOAD",
                    "origin": "THIRD_PARTY_DATASOURCE",
                },
                "origin": "THIRD_PARTY_DATASOURCE",
                "owner_type": "Commercial",
                "taskable": False,
                "terrestrial_id": "TERRESTRIAL-ID",
                "urls": ["URL1", "URL2"],
            },
            id_entity="ENTITY-ID",
            id_sensor="SENSOR-ID",
            origin="THIRD_PARTY_DATASOURCE",
            sensorcharacteristics=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sensor": "SENSOR-ID",
                    "source": "Bluestaq",
                    "id": "SENSORCHARACTERISTICS-ID",
                    "accept_sample_ranges": [3.01, 3.02],
                    "analog_to_digital_bit_size": 2,
                    "aperture": 2.23,
                    "asr_scan_rate": 20.23,
                    "atmos_receiver_loss": 0.5,
                    "atmos_transmission_loss": 0.5,
                    "avg_atmos_seeing_conditions": 10.23,
                    "az_angs": [135.1, 45.2],
                    "azimuth_rate": 0.3334,
                    "background_sky_radiance": 10.23,
                    "background_sky_vis_mag": 10.23,
                    "band": "BAND",
                    "bandwidth": 100.23,
                    "beam_order": ["vb1", "ob1"],
                    "beam_qty": 2,
                    "boresight": 20.23,
                    "boresight_off_angle": 20.23,
                    "center_wavelength": 4.56,
                    "collapsing_loss": 1.23,
                    "crit_shear": 47.1,
                    "dark_current": 12.3,
                    "delay_gates": [690.2, 690.3],
                    "description": "PROFILER DATA - PROFILE/SOUNDER DATA FROM PRIMARY WINDS SOURCE",
                    "detect_snr": 2.1,
                    "duty_cycle": 0.5,
                    "earth_limb_excl_hgt": 20.23,
                    "el_angs": [75.3, 75.4],
                    "elevation_rate_geolm": 0.9555,
                    "equipment_type": "PS",
                    "fan_beam_width": 3.1,
                    "fft": 4096,
                    "fgp_crit": 5,
                    "filter_mismatch_factor": 10.23,
                    "f_num": 1.23,
                    "focal_point": 20.23,
                    "h_fov": 20.23,
                    "h_res_pixels": 1000,
                    "k": 1.4,
                    "left_clock_angle": 20.23,
                    "left_geo_belt_limit": 20.23,
                    "location": "KENNEDY SPACE CENTER, FL",
                    "loop_gain": 150.1,
                    "lunar_excl_angle": 45.2,
                    "mag_dec": 45.23,
                    "magnitude_limit": 23.5,
                    "max_deviation_angle": 20.23,
                    "max_integration_time": 1.1,
                    "max_observable_range": 20.23,
                    "max_range_limit": 4972.1,
                    "max_wavelength": 7.89,
                    "min_integration_time": 0.3,
                    "min_range_limit": 165.1,
                    "min_signal_noise_ratio": 31.5,
                    "min_wavelength": 1.23,
                    "negative_range_rate_limit": -19.25,
                    "noise_figure": 10.23,
                    "non_coherent_integrated_pulses": 2,
                    "num_integrated_pulses": 10,
                    "num_integration_frames": 2,
                    "num_optical_integration_modes": 2,
                    "num_waveforms": 2,
                    "optical_integration_angular_rates": [15.1, 0.1],
                    "optical_integration_frames": [2.1, 3.1],
                    "optical_integration_pixel_binnings": [2.1, 1.1],
                    "optical_integration_sn_rs": [6.1, 6.1],
                    "optical_integration_times": [0.3, 1],
                    "optical_transmission": 0.5,
                    "pattern_absorption_loss": 1.23,
                    "pattern_scan_loss": 1.23,
                    "peak_power": 5000000.1,
                    "pixel_instantaneous_fov": 10.23,
                    "pixel_well_depth": 12,
                    "positive_range_rate_limit": 19.25,
                    "prf": 20.23,
                    "prob_detect_snr": 0.5,
                    "prob_false_alarm": 0.5,
                    "pulse_rep_periods": [153.8, 153.9],
                    "quantum_eff": 0.5,
                    "radar_frequency": 45300000000.1,
                    "radar_message_format": "DATA_FORMAT",
                    "radar_mur": 20.23,
                    "radar_pulse_widths": [20.23, 20.33],
                    "radio_frequency": 20.23,
                    "radome_loss": 1.23,
                    "range_gates": [51, 52],
                    "range_spacings": [690.2, 690.3],
                    "read_noise": 12,
                    "receive_gain": 10.2,
                    "receive_horiz_beam_width": 75.3,
                    "receive_loss": 1.23,
                    "receive_vert_beam_width": 75.4,
                    "ref_temp": 3.5,
                    "req_records": [0, 1],
                    "right_clock_angle": 20.23,
                    "right_geo_belt_limit": 20.23,
                    "run_mean_codes": [0, 5],
                    "signal_processing_loss": 1.23,
                    "site_code": "07",
                    "solar_excl_angle": 50.5,
                    "spec_avg_spectra_nums": [3, 4],
                    "system_noise_temperature": 3.5,
                    "taskable_range": 20.23,
                    "temp_med_filt_codes": [3, 4],
                    "test_number": "02022",
                    "tot_rec_nums": [5, 2],
                    "tower_height": 20.23,
                    "track_angle": 0.043,
                    "track_snr": 15.1,
                    "transmit_gain": 32.1,
                    "transmit_horiz_beam_width": 135.1,
                    "transmit_loss": 7.1,
                    "transmit_power": 190000.1,
                    "transmit_vert_beam_width": 45.2,
                    "true_north_corrector": 10,
                    "true_tilt": 20.23,
                    "twilight_angle": 7.5,
                    "vert_beam_flag": False,
                    "vert_gate_spacings": [149.1, 149.2],
                    "vert_gate_widths": [149.1, 149.2],
                    "v_fov": 20.23,
                    "v_res_pixels": 1000,
                    "waveform_bandwidths": [0.25, 0.25],
                    "waveform_loop_gains": [150.1, 155.1],
                    "waveform_max_ranges": [2000.1, 2000.1],
                    "waveform_min_ranges": [150.1, 150.1],
                    "waveform_pulse_widths": [100.1, 200.1],
                    "z1_max_range": 50.23,
                    "z1_min_range": 20.23,
                    "z2_max_range": 50.23,
                    "z2_min_range": 20.23,
                }
            ],
            sensorlimits_collection=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "id_sensor": "SENSORLIMITS-ID",
                    "id_sensor_limits": "SENSORLIMITS-ID",
                    "lower_left_azimuth_limit": 1.23,
                    "lower_left_elevation_limit": 1.23,
                    "lower_right_azimuth_limit": 1.23,
                    "lower_right_elevation_limit": 1.23,
                    "upper_left_azimuth_limit": 1.23,
                    "upper_left_elevation_limit": 1.23,
                    "upper_right_azimuth_limit": 1.23,
                    "upper_right_elevation_limit": 1.23,
                }
            ],
            sensor_number=1234,
            sensor_observation_type={
                "id": "3",
                "type": "5",
            },
            sensor_stats=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sensor": "idSensor",
                    "source": "Bluestaq",
                    "id": "SENSORSTATS-ID",
                    "last_ob_time": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
            sensor_type={
                "id": 12344411,
                "type": "Space Borne",
            },
            short_name="SNR-1",
        )
        assert sensor is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            sensor_name="SENSOR_NAME",
            source="some.user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = await response.parse()
        assert sensor is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            sensor_name="SENSOR_NAME",
            source="some.user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = await response.parse()
            assert sensor is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor = await async_client.sensor.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            sensor_name="SENSOR_NAME",
            source="some.user",
        )
        assert sensor is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor = await async_client.sensor.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            sensor_name="SENSOR_NAME",
            source="some.user",
            active=True,
            af_id="AF-ID",
            asr_type="SENSOR_TYPE",
            data_control="observations",
            entity={
                "classification_marking": "U",
                "data_mode": "TEST",
                "name": "Example name",
                "source": "Bluestaq",
                "type": "ONORBIT",
                "country_code": "US",
                "id_entity": "ENTITY-ID",
                "id_location": "LOCATION-ID",
                "id_on_orbit": "ONORBIT-ID",
                "id_operating_unit": "OPERATINGUNIT-ID",
                "location": {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "name": "Example location",
                    "source": "Bluestaq",
                    "altitude": 10.23,
                    "country_code": "US",
                    "id_location": "LOCATION-ID",
                    "lat": 45.23,
                    "lon": 179.1,
                    "origin": "THIRD_PARTY_DATASOURCE",
                },
                "on_orbit": {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "sat_no": 1,
                    "source": "Bluestaq",
                    "alt_name": "Alternate Name",
                    "category": "Lunar",
                    "common_name": "Example common name",
                    "constellation": "Big Dipper",
                    "country_code": "US",
                    "decay_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "id_on_orbit": "ONORBIT-ID",
                    "intl_des": "2021123ABC",
                    "launch_date": parse_date("2018-01-01"),
                    "launch_site_id": "LAUNCHSITE-ID",
                    "lifetime_years": 10,
                    "mission_number": "Expedition 1",
                    "object_type": "PAYLOAD",
                    "origin": "THIRD_PARTY_DATASOURCE",
                },
                "origin": "THIRD_PARTY_DATASOURCE",
                "owner_type": "Commercial",
                "taskable": False,
                "terrestrial_id": "TERRESTRIAL-ID",
                "urls": ["URL1", "URL2"],
            },
            id_entity="ENTITY-ID",
            id_sensor="SENSOR-ID",
            origin="THIRD_PARTY_DATASOURCE",
            sensorcharacteristics=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sensor": "SENSOR-ID",
                    "source": "Bluestaq",
                    "id": "SENSORCHARACTERISTICS-ID",
                    "accept_sample_ranges": [3.01, 3.02],
                    "analog_to_digital_bit_size": 2,
                    "aperture": 2.23,
                    "asr_scan_rate": 20.23,
                    "atmos_receiver_loss": 0.5,
                    "atmos_transmission_loss": 0.5,
                    "avg_atmos_seeing_conditions": 10.23,
                    "az_angs": [135.1, 45.2],
                    "azimuth_rate": 0.3334,
                    "background_sky_radiance": 10.23,
                    "background_sky_vis_mag": 10.23,
                    "band": "BAND",
                    "bandwidth": 100.23,
                    "beam_order": ["vb1", "ob1"],
                    "beam_qty": 2,
                    "boresight": 20.23,
                    "boresight_off_angle": 20.23,
                    "center_wavelength": 4.56,
                    "collapsing_loss": 1.23,
                    "crit_shear": 47.1,
                    "dark_current": 12.3,
                    "delay_gates": [690.2, 690.3],
                    "description": "PROFILER DATA - PROFILE/SOUNDER DATA FROM PRIMARY WINDS SOURCE",
                    "detect_snr": 2.1,
                    "duty_cycle": 0.5,
                    "earth_limb_excl_hgt": 20.23,
                    "el_angs": [75.3, 75.4],
                    "elevation_rate_geolm": 0.9555,
                    "equipment_type": "PS",
                    "fan_beam_width": 3.1,
                    "fft": 4096,
                    "fgp_crit": 5,
                    "filter_mismatch_factor": 10.23,
                    "f_num": 1.23,
                    "focal_point": 20.23,
                    "h_fov": 20.23,
                    "h_res_pixels": 1000,
                    "k": 1.4,
                    "left_clock_angle": 20.23,
                    "left_geo_belt_limit": 20.23,
                    "location": "KENNEDY SPACE CENTER, FL",
                    "loop_gain": 150.1,
                    "lunar_excl_angle": 45.2,
                    "mag_dec": 45.23,
                    "magnitude_limit": 23.5,
                    "max_deviation_angle": 20.23,
                    "max_integration_time": 1.1,
                    "max_observable_range": 20.23,
                    "max_range_limit": 4972.1,
                    "max_wavelength": 7.89,
                    "min_integration_time": 0.3,
                    "min_range_limit": 165.1,
                    "min_signal_noise_ratio": 31.5,
                    "min_wavelength": 1.23,
                    "negative_range_rate_limit": -19.25,
                    "noise_figure": 10.23,
                    "non_coherent_integrated_pulses": 2,
                    "num_integrated_pulses": 10,
                    "num_integration_frames": 2,
                    "num_optical_integration_modes": 2,
                    "num_waveforms": 2,
                    "optical_integration_angular_rates": [15.1, 0.1],
                    "optical_integration_frames": [2.1, 3.1],
                    "optical_integration_pixel_binnings": [2.1, 1.1],
                    "optical_integration_sn_rs": [6.1, 6.1],
                    "optical_integration_times": [0.3, 1],
                    "optical_transmission": 0.5,
                    "pattern_absorption_loss": 1.23,
                    "pattern_scan_loss": 1.23,
                    "peak_power": 5000000.1,
                    "pixel_instantaneous_fov": 10.23,
                    "pixel_well_depth": 12,
                    "positive_range_rate_limit": 19.25,
                    "prf": 20.23,
                    "prob_detect_snr": 0.5,
                    "prob_false_alarm": 0.5,
                    "pulse_rep_periods": [153.8, 153.9],
                    "quantum_eff": 0.5,
                    "radar_frequency": 45300000000.1,
                    "radar_message_format": "DATA_FORMAT",
                    "radar_mur": 20.23,
                    "radar_pulse_widths": [20.23, 20.33],
                    "radio_frequency": 20.23,
                    "radome_loss": 1.23,
                    "range_gates": [51, 52],
                    "range_spacings": [690.2, 690.3],
                    "read_noise": 12,
                    "receive_gain": 10.2,
                    "receive_horiz_beam_width": 75.3,
                    "receive_loss": 1.23,
                    "receive_vert_beam_width": 75.4,
                    "ref_temp": 3.5,
                    "req_records": [0, 1],
                    "right_clock_angle": 20.23,
                    "right_geo_belt_limit": 20.23,
                    "run_mean_codes": [0, 5],
                    "signal_processing_loss": 1.23,
                    "site_code": "07",
                    "solar_excl_angle": 50.5,
                    "spec_avg_spectra_nums": [3, 4],
                    "system_noise_temperature": 3.5,
                    "taskable_range": 20.23,
                    "temp_med_filt_codes": [3, 4],
                    "test_number": "02022",
                    "tot_rec_nums": [5, 2],
                    "tower_height": 20.23,
                    "track_angle": 0.043,
                    "track_snr": 15.1,
                    "transmit_gain": 32.1,
                    "transmit_horiz_beam_width": 135.1,
                    "transmit_loss": 7.1,
                    "transmit_power": 190000.1,
                    "transmit_vert_beam_width": 45.2,
                    "true_north_corrector": 10,
                    "true_tilt": 20.23,
                    "twilight_angle": 7.5,
                    "vert_beam_flag": False,
                    "vert_gate_spacings": [149.1, 149.2],
                    "vert_gate_widths": [149.1, 149.2],
                    "v_fov": 20.23,
                    "v_res_pixels": 1000,
                    "waveform_bandwidths": [0.25, 0.25],
                    "waveform_loop_gains": [150.1, 155.1],
                    "waveform_max_ranges": [2000.1, 2000.1],
                    "waveform_min_ranges": [150.1, 150.1],
                    "waveform_pulse_widths": [100.1, 200.1],
                    "z1_max_range": 50.23,
                    "z1_min_range": 20.23,
                    "z2_max_range": 50.23,
                    "z2_min_range": 20.23,
                }
            ],
            sensorlimits_collection=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "id_sensor": "SENSORLIMITS-ID",
                    "id_sensor_limits": "SENSORLIMITS-ID",
                    "lower_left_azimuth_limit": 1.23,
                    "lower_left_elevation_limit": 1.23,
                    "lower_right_azimuth_limit": 1.23,
                    "lower_right_elevation_limit": 1.23,
                    "upper_left_azimuth_limit": 1.23,
                    "upper_left_elevation_limit": 1.23,
                    "upper_right_azimuth_limit": 1.23,
                    "upper_right_elevation_limit": 1.23,
                }
            ],
            sensor_number=1234,
            sensor_observation_type={
                "id": "3",
                "type": "5",
            },
            sensor_stats=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sensor": "idSensor",
                    "source": "Bluestaq",
                    "id": "SENSORSTATS-ID",
                    "last_ob_time": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
            sensor_type={
                "id": 12344411,
                "type": "Space Borne",
            },
            short_name="SNR-1",
        )
        assert sensor is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor.with_raw_response.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            sensor_name="SENSOR_NAME",
            source="some.user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = await response.parse()
        assert sensor is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor.with_streaming_response.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            sensor_name="SENSOR_NAME",
            source="some.user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = await response.parse()
            assert sensor is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sensor.with_raw_response.update(
                id="",
                classification_marking="U",
                data_mode="TEST",
                sensor_name="SENSOR_NAME",
                source="some.user",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor = await async_client.sensor.list()
        assert_matches_type(AsyncOffsetPage[SensorListResponse], sensor, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor = await async_client.sensor.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[SensorListResponse], sensor, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = await response.parse()
        assert_matches_type(AsyncOffsetPage[SensorListResponse], sensor, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = await response.parse()
            assert_matches_type(AsyncOffsetPage[SensorListResponse], sensor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor = await async_client.sensor.delete(
            "id",
        )
        assert sensor is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = await response.parse()
        assert sensor is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = await response.parse()
            assert sensor is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sensor.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor = await async_client.sensor.count()
        assert_matches_type(str, sensor, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor = await async_client.sensor.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, sensor, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = await response.parse()
        assert_matches_type(str, sensor, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = await response.parse()
            assert_matches_type(str, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor = await async_client.sensor.get(
            id="id",
        )
        assert_matches_type(SensorGetResponse, sensor, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor = await async_client.sensor.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SensorGetResponse, sensor, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = await response.parse()
        assert_matches_type(SensorGetResponse, sensor, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = await response.parse()
            assert_matches_type(SensorGetResponse, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sensor.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor = await async_client.sensor.queryhelp()
        assert_matches_type(SensorQueryhelpResponse, sensor, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = await response.parse()
        assert_matches_type(SensorQueryhelpResponse, sensor, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = await response.parse()
            assert_matches_type(SensorQueryhelpResponse, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor = await async_client.sensor.tuple(
            columns="columns",
        )
        assert_matches_type(SensorTupleResponse, sensor, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor = await async_client.sensor.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SensorTupleResponse, sensor, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = await response.parse()
        assert_matches_type(SensorTupleResponse, sensor, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = await response.parse()
            assert_matches_type(SensorTupleResponse, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True
