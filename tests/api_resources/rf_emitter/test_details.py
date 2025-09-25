# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.rf_emitter import (
    DetailGetResponse,
    DetailListResponse,
    DetailTupleResponse,
    DetailQueryhelpResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        detail = client.rf_emitter.details.create(
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
        )
        assert detail is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        detail = client.rf_emitter.details.create(
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
            id="ad88770b-d824-443f-bdce-5f9e3fa500a9",
            alternate_facility_name="ALTERNATE_FACILITY_NAME",
            alt_name="ALTERNATE_NAME",
            amplifier={
                "device_identifier": "1200W_Amplifier_GE",
                "manufacturer": "General Electric",
                "model_name": "Model 2600",
                "power": 1200.1,
            },
            antennas=[
                {
                    "antenna_diameter": 20.23,
                    "antenna_size": [1.1, 2.2],
                    "az_el_fixed": True,
                    "feeds": [
                        {
                            "freq_max": 43500.1,
                            "freq_min": 39500.1,
                            "name": "Feed A",
                            "polarization": "HORIZONTAL",
                        }
                    ],
                    "fixed_azimuth": 5.1,
                    "fixed_elevation": 10.1,
                    "max_azimuths": [359.1, 359.1],
                    "max_elevation": 88.1,
                    "min_azimuths": [5.1, 7.5],
                    "min_elevation": 10.1,
                    "name": "ds1Rotor",
                    "receiver_channels": [
                        {
                            "bandwidth": 0.51,
                            "channel_num": "315",
                            "device_identifier": "MMS1",
                            "freq_max": 43500.1,
                            "freq_min": 39500.1,
                            "max_bandwidth": 100.1,
                            "min_bandwidth": 0.05,
                            "sensitivity": 10.23,
                        }
                    ],
                    "transmit_channels": [
                        {
                            "power": 100.23,
                            "bandwidth": 0.125,
                            "channel_num": "12",
                            "device_identifier": "TX1-B4-778",
                            "freq": 42000.1,
                            "freq_max": 43500.1,
                            "freq_min": 39500.1,
                            "hardware_sample_rate": 192000,
                            "max_bandwidth": 100.1,
                            "max_gain": 20.1,
                            "min_bandwidth": 0.05,
                            "min_gain": 0.1,
                            "sample_rates": [192000, 9216000],
                        }
                    ],
                }
            ],
            barrage_noise_bandwidth=5.23,
            bit_run_time=120.1,
            description="DESCRIPTION",
            designator="DESIGNATOR",
            doppler_noise=10.23,
            drfm_instantaneous_bandwidth=20.23,
            family="FAMILY",
            fixed_attenuation=5.1,
            id_manufacturer_org="MANUFACTURERORG-ID",
            id_production_facility_location="PRODUCTIONFACILITYLOCATION-ID",
            loaned_to_cocom="SPACEFOR-STRATNORTH",
            notes="NOTES",
            num_bits=256,
            num_channels=10,
            origin="THIRD_PARTY_DATASOURCE",
            power_offsets=[
                {
                    "frequency_band": "KU",
                    "power_offset": -5.1,
                }
            ],
            prep_time=60.1,
            primary_cocom="SPACESOC",
            production_facility_name="PRODUCTION_FACILITY",
            receiver_type="RECEIVER_TYPE",
            secondary_notes="MORE_NOTES",
            services=[
                {
                    "name": "tlc-freqcontrol",
                    "version": "17.2.5_build72199",
                }
            ],
            system_sensitivity_end=150.23,
            system_sensitivity_start=50.32,
            ttps=[
                {
                    "output_signal_name": "SIGNAL_A",
                    "technique_definitions": [
                        {
                            "name": "SIGNAL TUNE",
                            "param_definitions": [
                                {
                                    "default_value": "444.0",
                                    "max": 1000.1,
                                    "min": 0.1,
                                    "name": "CENTER_FREQ",
                                    "optional": False,
                                    "type": "DOUBLE",
                                    "units": "hertz",
                                    "valid_values": ["100.1", "444.1", "1000.1"],
                                }
                            ],
                        }
                    ],
                }
            ],
            urls=["TAG1", "TAG2"],
        )
        assert detail is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.rf_emitter.details.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = response.parse()
        assert detail is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.rf_emitter.details.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = response.parse()
            assert detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        detail = client.rf_emitter.details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
        )
        assert detail is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        detail = client.rf_emitter.details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
            body_id="ad88770b-d824-443f-bdce-5f9e3fa500a9",
            alternate_facility_name="ALTERNATE_FACILITY_NAME",
            alt_name="ALTERNATE_NAME",
            amplifier={
                "device_identifier": "1200W_Amplifier_GE",
                "manufacturer": "General Electric",
                "model_name": "Model 2600",
                "power": 1200.1,
            },
            antennas=[
                {
                    "antenna_diameter": 20.23,
                    "antenna_size": [1.1, 2.2],
                    "az_el_fixed": True,
                    "feeds": [
                        {
                            "freq_max": 43500.1,
                            "freq_min": 39500.1,
                            "name": "Feed A",
                            "polarization": "HORIZONTAL",
                        }
                    ],
                    "fixed_azimuth": 5.1,
                    "fixed_elevation": 10.1,
                    "max_azimuths": [359.1, 359.1],
                    "max_elevation": 88.1,
                    "min_azimuths": [5.1, 7.5],
                    "min_elevation": 10.1,
                    "name": "ds1Rotor",
                    "receiver_channels": [
                        {
                            "bandwidth": 0.51,
                            "channel_num": "315",
                            "device_identifier": "MMS1",
                            "freq_max": 43500.1,
                            "freq_min": 39500.1,
                            "max_bandwidth": 100.1,
                            "min_bandwidth": 0.05,
                            "sensitivity": 10.23,
                        }
                    ],
                    "transmit_channels": [
                        {
                            "power": 100.23,
                            "bandwidth": 0.125,
                            "channel_num": "12",
                            "device_identifier": "TX1-B4-778",
                            "freq": 42000.1,
                            "freq_max": 43500.1,
                            "freq_min": 39500.1,
                            "hardware_sample_rate": 192000,
                            "max_bandwidth": 100.1,
                            "max_gain": 20.1,
                            "min_bandwidth": 0.05,
                            "min_gain": 0.1,
                            "sample_rates": [192000, 9216000],
                        }
                    ],
                }
            ],
            barrage_noise_bandwidth=5.23,
            bit_run_time=120.1,
            description="DESCRIPTION",
            designator="DESIGNATOR",
            doppler_noise=10.23,
            drfm_instantaneous_bandwidth=20.23,
            family="FAMILY",
            fixed_attenuation=5.1,
            id_manufacturer_org="MANUFACTURERORG-ID",
            id_production_facility_location="PRODUCTIONFACILITYLOCATION-ID",
            loaned_to_cocom="SPACEFOR-STRATNORTH",
            notes="NOTES",
            num_bits=256,
            num_channels=10,
            origin="THIRD_PARTY_DATASOURCE",
            power_offsets=[
                {
                    "frequency_band": "KU",
                    "power_offset": -5.1,
                }
            ],
            prep_time=60.1,
            primary_cocom="SPACESOC",
            production_facility_name="PRODUCTION_FACILITY",
            receiver_type="RECEIVER_TYPE",
            secondary_notes="MORE_NOTES",
            services=[
                {
                    "name": "tlc-freqcontrol",
                    "version": "17.2.5_build72199",
                }
            ],
            system_sensitivity_end=150.23,
            system_sensitivity_start=50.32,
            ttps=[
                {
                    "output_signal_name": "SIGNAL_A",
                    "technique_definitions": [
                        {
                            "name": "SIGNAL TUNE",
                            "param_definitions": [
                                {
                                    "default_value": "444.0",
                                    "max": 1000.1,
                                    "min": 0.1,
                                    "name": "CENTER_FREQ",
                                    "optional": False,
                                    "type": "DOUBLE",
                                    "units": "hertz",
                                    "valid_values": ["100.1", "444.1", "1000.1"],
                                }
                            ],
                        }
                    ],
                }
            ],
            urls=["TAG1", "TAG2"],
        )
        assert detail is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.rf_emitter.details.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = response.parse()
        assert detail is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.rf_emitter.details.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = response.parse()
            assert detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.rf_emitter.details.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_rf_emitter="RFEMITTER-ID",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        detail = client.rf_emitter.details.list()
        assert_matches_type(SyncOffsetPage[DetailListResponse], detail, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        detail = client.rf_emitter.details.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[DetailListResponse], detail, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.rf_emitter.details.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = response.parse()
        assert_matches_type(SyncOffsetPage[DetailListResponse], detail, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.rf_emitter.details.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = response.parse()
            assert_matches_type(SyncOffsetPage[DetailListResponse], detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        detail = client.rf_emitter.details.delete(
            "id",
        )
        assert detail is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.rf_emitter.details.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = response.parse()
        assert detail is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.rf_emitter.details.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = response.parse()
            assert detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rf_emitter.details.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        detail = client.rf_emitter.details.count()
        assert_matches_type(str, detail, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        detail = client.rf_emitter.details.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, detail, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.rf_emitter.details.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = response.parse()
        assert_matches_type(str, detail, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.rf_emitter.details.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = response.parse()
            assert_matches_type(str, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        detail = client.rf_emitter.details.get(
            id="id",
        )
        assert_matches_type(DetailGetResponse, detail, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        detail = client.rf_emitter.details.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(DetailGetResponse, detail, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.rf_emitter.details.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = response.parse()
        assert_matches_type(DetailGetResponse, detail, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.rf_emitter.details.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = response.parse()
            assert_matches_type(DetailGetResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rf_emitter.details.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        detail = client.rf_emitter.details.queryhelp()
        assert_matches_type(DetailQueryhelpResponse, detail, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.rf_emitter.details.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = response.parse()
        assert_matches_type(DetailQueryhelpResponse, detail, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.rf_emitter.details.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = response.parse()
            assert_matches_type(DetailQueryhelpResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        detail = client.rf_emitter.details.tuple(
            columns="columns",
        )
        assert_matches_type(DetailTupleResponse, detail, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        detail = client.rf_emitter.details.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(DetailTupleResponse, detail, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.rf_emitter.details.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = response.parse()
        assert_matches_type(DetailTupleResponse, detail, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.rf_emitter.details.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = response.parse()
            assert_matches_type(DetailTupleResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDetails:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        detail = await async_client.rf_emitter.details.create(
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
        )
        assert detail is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        detail = await async_client.rf_emitter.details.create(
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
            id="ad88770b-d824-443f-bdce-5f9e3fa500a9",
            alternate_facility_name="ALTERNATE_FACILITY_NAME",
            alt_name="ALTERNATE_NAME",
            amplifier={
                "device_identifier": "1200W_Amplifier_GE",
                "manufacturer": "General Electric",
                "model_name": "Model 2600",
                "power": 1200.1,
            },
            antennas=[
                {
                    "antenna_diameter": 20.23,
                    "antenna_size": [1.1, 2.2],
                    "az_el_fixed": True,
                    "feeds": [
                        {
                            "freq_max": 43500.1,
                            "freq_min": 39500.1,
                            "name": "Feed A",
                            "polarization": "HORIZONTAL",
                        }
                    ],
                    "fixed_azimuth": 5.1,
                    "fixed_elevation": 10.1,
                    "max_azimuths": [359.1, 359.1],
                    "max_elevation": 88.1,
                    "min_azimuths": [5.1, 7.5],
                    "min_elevation": 10.1,
                    "name": "ds1Rotor",
                    "receiver_channels": [
                        {
                            "bandwidth": 0.51,
                            "channel_num": "315",
                            "device_identifier": "MMS1",
                            "freq_max": 43500.1,
                            "freq_min": 39500.1,
                            "max_bandwidth": 100.1,
                            "min_bandwidth": 0.05,
                            "sensitivity": 10.23,
                        }
                    ],
                    "transmit_channels": [
                        {
                            "power": 100.23,
                            "bandwidth": 0.125,
                            "channel_num": "12",
                            "device_identifier": "TX1-B4-778",
                            "freq": 42000.1,
                            "freq_max": 43500.1,
                            "freq_min": 39500.1,
                            "hardware_sample_rate": 192000,
                            "max_bandwidth": 100.1,
                            "max_gain": 20.1,
                            "min_bandwidth": 0.05,
                            "min_gain": 0.1,
                            "sample_rates": [192000, 9216000],
                        }
                    ],
                }
            ],
            barrage_noise_bandwidth=5.23,
            bit_run_time=120.1,
            description="DESCRIPTION",
            designator="DESIGNATOR",
            doppler_noise=10.23,
            drfm_instantaneous_bandwidth=20.23,
            family="FAMILY",
            fixed_attenuation=5.1,
            id_manufacturer_org="MANUFACTURERORG-ID",
            id_production_facility_location="PRODUCTIONFACILITYLOCATION-ID",
            loaned_to_cocom="SPACEFOR-STRATNORTH",
            notes="NOTES",
            num_bits=256,
            num_channels=10,
            origin="THIRD_PARTY_DATASOURCE",
            power_offsets=[
                {
                    "frequency_band": "KU",
                    "power_offset": -5.1,
                }
            ],
            prep_time=60.1,
            primary_cocom="SPACESOC",
            production_facility_name="PRODUCTION_FACILITY",
            receiver_type="RECEIVER_TYPE",
            secondary_notes="MORE_NOTES",
            services=[
                {
                    "name": "tlc-freqcontrol",
                    "version": "17.2.5_build72199",
                }
            ],
            system_sensitivity_end=150.23,
            system_sensitivity_start=50.32,
            ttps=[
                {
                    "output_signal_name": "SIGNAL_A",
                    "technique_definitions": [
                        {
                            "name": "SIGNAL TUNE",
                            "param_definitions": [
                                {
                                    "default_value": "444.0",
                                    "max": 1000.1,
                                    "min": 0.1,
                                    "name": "CENTER_FREQ",
                                    "optional": False,
                                    "type": "DOUBLE",
                                    "units": "hertz",
                                    "valid_values": ["100.1", "444.1", "1000.1"],
                                }
                            ],
                        }
                    ],
                }
            ],
            urls=["TAG1", "TAG2"],
        )
        assert detail is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rf_emitter.details.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = await response.parse()
        assert detail is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rf_emitter.details.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = await response.parse()
            assert detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        detail = await async_client.rf_emitter.details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
        )
        assert detail is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        detail = await async_client.rf_emitter.details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
            body_id="ad88770b-d824-443f-bdce-5f9e3fa500a9",
            alternate_facility_name="ALTERNATE_FACILITY_NAME",
            alt_name="ALTERNATE_NAME",
            amplifier={
                "device_identifier": "1200W_Amplifier_GE",
                "manufacturer": "General Electric",
                "model_name": "Model 2600",
                "power": 1200.1,
            },
            antennas=[
                {
                    "antenna_diameter": 20.23,
                    "antenna_size": [1.1, 2.2],
                    "az_el_fixed": True,
                    "feeds": [
                        {
                            "freq_max": 43500.1,
                            "freq_min": 39500.1,
                            "name": "Feed A",
                            "polarization": "HORIZONTAL",
                        }
                    ],
                    "fixed_azimuth": 5.1,
                    "fixed_elevation": 10.1,
                    "max_azimuths": [359.1, 359.1],
                    "max_elevation": 88.1,
                    "min_azimuths": [5.1, 7.5],
                    "min_elevation": 10.1,
                    "name": "ds1Rotor",
                    "receiver_channels": [
                        {
                            "bandwidth": 0.51,
                            "channel_num": "315",
                            "device_identifier": "MMS1",
                            "freq_max": 43500.1,
                            "freq_min": 39500.1,
                            "max_bandwidth": 100.1,
                            "min_bandwidth": 0.05,
                            "sensitivity": 10.23,
                        }
                    ],
                    "transmit_channels": [
                        {
                            "power": 100.23,
                            "bandwidth": 0.125,
                            "channel_num": "12",
                            "device_identifier": "TX1-B4-778",
                            "freq": 42000.1,
                            "freq_max": 43500.1,
                            "freq_min": 39500.1,
                            "hardware_sample_rate": 192000,
                            "max_bandwidth": 100.1,
                            "max_gain": 20.1,
                            "min_bandwidth": 0.05,
                            "min_gain": 0.1,
                            "sample_rates": [192000, 9216000],
                        }
                    ],
                }
            ],
            barrage_noise_bandwidth=5.23,
            bit_run_time=120.1,
            description="DESCRIPTION",
            designator="DESIGNATOR",
            doppler_noise=10.23,
            drfm_instantaneous_bandwidth=20.23,
            family="FAMILY",
            fixed_attenuation=5.1,
            id_manufacturer_org="MANUFACTURERORG-ID",
            id_production_facility_location="PRODUCTIONFACILITYLOCATION-ID",
            loaned_to_cocom="SPACEFOR-STRATNORTH",
            notes="NOTES",
            num_bits=256,
            num_channels=10,
            origin="THIRD_PARTY_DATASOURCE",
            power_offsets=[
                {
                    "frequency_band": "KU",
                    "power_offset": -5.1,
                }
            ],
            prep_time=60.1,
            primary_cocom="SPACESOC",
            production_facility_name="PRODUCTION_FACILITY",
            receiver_type="RECEIVER_TYPE",
            secondary_notes="MORE_NOTES",
            services=[
                {
                    "name": "tlc-freqcontrol",
                    "version": "17.2.5_build72199",
                }
            ],
            system_sensitivity_end=150.23,
            system_sensitivity_start=50.32,
            ttps=[
                {
                    "output_signal_name": "SIGNAL_A",
                    "technique_definitions": [
                        {
                            "name": "SIGNAL TUNE",
                            "param_definitions": [
                                {
                                    "default_value": "444.0",
                                    "max": 1000.1,
                                    "min": 0.1,
                                    "name": "CENTER_FREQ",
                                    "optional": False,
                                    "type": "DOUBLE",
                                    "units": "hertz",
                                    "valid_values": ["100.1", "444.1", "1000.1"],
                                }
                            ],
                        }
                    ],
                }
            ],
            urls=["TAG1", "TAG2"],
        )
        assert detail is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rf_emitter.details.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = await response.parse()
        assert detail is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rf_emitter.details.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = await response.parse()
            assert detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.rf_emitter.details.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_rf_emitter="RFEMITTER-ID",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        detail = await async_client.rf_emitter.details.list()
        assert_matches_type(AsyncOffsetPage[DetailListResponse], detail, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        detail = await async_client.rf_emitter.details.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[DetailListResponse], detail, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rf_emitter.details.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = await response.parse()
        assert_matches_type(AsyncOffsetPage[DetailListResponse], detail, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rf_emitter.details.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = await response.parse()
            assert_matches_type(AsyncOffsetPage[DetailListResponse], detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        detail = await async_client.rf_emitter.details.delete(
            "id",
        )
        assert detail is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rf_emitter.details.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = await response.parse()
        assert detail is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rf_emitter.details.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = await response.parse()
            assert detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rf_emitter.details.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        detail = await async_client.rf_emitter.details.count()
        assert_matches_type(str, detail, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        detail = await async_client.rf_emitter.details.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, detail, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rf_emitter.details.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = await response.parse()
        assert_matches_type(str, detail, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rf_emitter.details.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = await response.parse()
            assert_matches_type(str, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        detail = await async_client.rf_emitter.details.get(
            id="id",
        )
        assert_matches_type(DetailGetResponse, detail, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        detail = await async_client.rf_emitter.details.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(DetailGetResponse, detail, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rf_emitter.details.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = await response.parse()
        assert_matches_type(DetailGetResponse, detail, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rf_emitter.details.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = await response.parse()
            assert_matches_type(DetailGetResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rf_emitter.details.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        detail = await async_client.rf_emitter.details.queryhelp()
        assert_matches_type(DetailQueryhelpResponse, detail, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rf_emitter.details.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = await response.parse()
        assert_matches_type(DetailQueryhelpResponse, detail, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rf_emitter.details.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = await response.parse()
            assert_matches_type(DetailQueryhelpResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        detail = await async_client.rf_emitter.details.tuple(
            columns="columns",
        )
        assert_matches_type(DetailTupleResponse, detail, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        detail = await async_client.rf_emitter.details.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(DetailTupleResponse, detail, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rf_emitter.details.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = await response.parse()
        assert_matches_type(DetailTupleResponse, detail, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rf_emitter.details.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = await response.parse()
            assert_matches_type(DetailTupleResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True
