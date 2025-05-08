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
    RfObservationGetResponse,
    RfObservationListResponse,
    RfObservationTupleResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRfObservation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        rf_observation = client.observations.rf_observation.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            type="RF",
        )
        assert rf_observation is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        rf_observation = client.observations.rf_observation.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            type="RF",
            id="RFOBSERVATION-ID",
            antenna_name="Antenna1",
            azimuth=10.1,
            azimuth_measured=True,
            azimuth_rate=1.1,
            azimuth_unc=2.1,
            bandwidth=10.1,
            baud_rate=10.1,
            baud_rates=[1.1, 2.2],
            bit_error_rate=10.1,
            carrier_standard="DVB-S2",
            channel=10,
            chip_rates=[1.1, 2.2],
            code_fills=["TAG1", "TAG2"],
            code_lengths=[1.1, 2.2],
            code_taps=["TAG1", "TAG2"],
            collection_mode="SURVEY",
            confidence=10.1,
            confidences=[1.1, 2.2],
            constellation_x_points=[1.1, 2.2],
            constellation_y_points=[1.1, 2.2],
            descriptor="descriptor",
            detection_status="DETECTED",
            detection_statuses=["DETECTED"],
            eirp=10.1,
            elevation=10.1,
            elevation_measured=True,
            elevation_rate=10.1,
            elevation_unc=10.1,
            elnot="Ex. ELINT",
            end_frequency=10.1,
            frequencies=[1.1, 2.2],
            frequency=10.1,
            frequency_shift=10.1,
            id_sensor="SENSOR-ID",
            incoming=False,
            inner_coding_rate=7,
            max_psd=10.1,
            min_psd=10.1,
            modulation="Auto",
            noise_pwr_density=10.1,
            nominal_bandwidth=10.1,
            nominal_eirp=10.1,
            nominal_frequency=10.1,
            nominal_power_over_noise=10.1,
            nominal_snr=10.1,
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIG-OBJECT-ID",
            orig_sensor_id="ORIG-SENSOR-ID",
            outer_coding_rate=4,
            peak=False,
            pgri=10.1,
            pn_orders=[1, 2],
            polarity=10.1,
            polarity_type="H",
            power_over_noise=10.1,
            powers=[1.1, 2.2],
            range=10.1,
            range_measured=True,
            range_rate=10.1,
            range_rate_measured=True,
            range_rate_unc=10.1,
            range_unc=10.1,
            raw_file_uri="Example URI",
            reference_level=10.1,
            relative_carrier_power=10.1,
            relative_noise_floor=10.1,
            resolution_bandwidth=10.1,
            sat_no=32258,
            senalt=10.1,
            senlat=45.2,
            senlon=80.3,
            signal_ids=["ID1", "ID2"],
            snr=10.1,
            snrs=[1.1, 2.2],
            spectrum_analyzer_power=10.1,
            start_frequency=10.1,
            switch_point=10,
            symbol_to_noise_ratio=10.1,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            task_id="TASK-ID",
            telemetry_ids=["ID1", "ID2"],
            track_id="TRACK-ID",
            track_range=10.1,
            transaction_id="TRANSACTION-ID",
            transmit_filter_roll_off=10.1,
            transmit_filter_type="RRC",
            transponder="TRANSPONDER-A",
            uct=False,
            url="https://some-url",
            video_bandwidth=10.1,
        )
        assert rf_observation is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.observations.rf_observation.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            type="RF",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_observation = response.parse()
        assert rf_observation is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.observations.rf_observation.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            type="RF",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_observation = response.parse()
            assert rf_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        rf_observation = client.observations.rf_observation.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[RfObservationListResponse], rf_observation, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        rf_observation = client.observations.rf_observation.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[RfObservationListResponse], rf_observation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.observations.rf_observation.with_raw_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_observation = response.parse()
        assert_matches_type(SyncOffsetPage[RfObservationListResponse], rf_observation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.observations.rf_observation.with_streaming_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_observation = response.parse()
            assert_matches_type(SyncOffsetPage[RfObservationListResponse], rf_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        rf_observation = client.observations.rf_observation.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, rf_observation, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        rf_observation = client.observations.rf_observation.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, rf_observation, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.observations.rf_observation.with_raw_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_observation = response.parse()
        assert_matches_type(str, rf_observation, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.observations.rf_observation.with_streaming_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_observation = response.parse()
            assert_matches_type(str, rf_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        rf_observation = client.observations.rf_observation.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                    "type": "RF",
                }
            ],
        )
        assert rf_observation is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.observations.rf_observation.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                    "type": "RF",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_observation = response.parse()
        assert rf_observation is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.observations.rf_observation.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                    "type": "RF",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_observation = response.parse()
            assert rf_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        rf_observation = client.observations.rf_observation.get(
            id="id",
        )
        assert_matches_type(RfObservationGetResponse, rf_observation, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        rf_observation = client.observations.rf_observation.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(RfObservationGetResponse, rf_observation, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.observations.rf_observation.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_observation = response.parse()
        assert_matches_type(RfObservationGetResponse, rf_observation, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.observations.rf_observation.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_observation = response.parse()
            assert_matches_type(RfObservationGetResponse, rf_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.observations.rf_observation.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        rf_observation = client.observations.rf_observation.queryhelp()
        assert rf_observation is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.observations.rf_observation.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_observation = response.parse()
        assert rf_observation is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.observations.rf_observation.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_observation = response.parse()
            assert rf_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        rf_observation = client.observations.rf_observation.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(RfObservationTupleResponse, rf_observation, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        rf_observation = client.observations.rf_observation.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(RfObservationTupleResponse, rf_observation, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.observations.rf_observation.with_raw_response.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_observation = response.parse()
        assert_matches_type(RfObservationTupleResponse, rf_observation, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.observations.rf_observation.with_streaming_response.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_observation = response.parse()
            assert_matches_type(RfObservationTupleResponse, rf_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        rf_observation = client.observations.rf_observation.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                    "type": "RF",
                }
            ],
        )
        assert rf_observation is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.observations.rf_observation.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                    "type": "RF",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_observation = response.parse()
        assert rf_observation is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.observations.rf_observation.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                    "type": "RF",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_observation = response.parse()
            assert rf_observation is None

        assert cast(Any, response.is_closed) is True


class TestAsyncRfObservation:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_observation = await async_client.observations.rf_observation.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            type="RF",
        )
        assert rf_observation is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_observation = await async_client.observations.rf_observation.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            type="RF",
            id="RFOBSERVATION-ID",
            antenna_name="Antenna1",
            azimuth=10.1,
            azimuth_measured=True,
            azimuth_rate=1.1,
            azimuth_unc=2.1,
            bandwidth=10.1,
            baud_rate=10.1,
            baud_rates=[1.1, 2.2],
            bit_error_rate=10.1,
            carrier_standard="DVB-S2",
            channel=10,
            chip_rates=[1.1, 2.2],
            code_fills=["TAG1", "TAG2"],
            code_lengths=[1.1, 2.2],
            code_taps=["TAG1", "TAG2"],
            collection_mode="SURVEY",
            confidence=10.1,
            confidences=[1.1, 2.2],
            constellation_x_points=[1.1, 2.2],
            constellation_y_points=[1.1, 2.2],
            descriptor="descriptor",
            detection_status="DETECTED",
            detection_statuses=["DETECTED"],
            eirp=10.1,
            elevation=10.1,
            elevation_measured=True,
            elevation_rate=10.1,
            elevation_unc=10.1,
            elnot="Ex. ELINT",
            end_frequency=10.1,
            frequencies=[1.1, 2.2],
            frequency=10.1,
            frequency_shift=10.1,
            id_sensor="SENSOR-ID",
            incoming=False,
            inner_coding_rate=7,
            max_psd=10.1,
            min_psd=10.1,
            modulation="Auto",
            noise_pwr_density=10.1,
            nominal_bandwidth=10.1,
            nominal_eirp=10.1,
            nominal_frequency=10.1,
            nominal_power_over_noise=10.1,
            nominal_snr=10.1,
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIG-OBJECT-ID",
            orig_sensor_id="ORIG-SENSOR-ID",
            outer_coding_rate=4,
            peak=False,
            pgri=10.1,
            pn_orders=[1, 2],
            polarity=10.1,
            polarity_type="H",
            power_over_noise=10.1,
            powers=[1.1, 2.2],
            range=10.1,
            range_measured=True,
            range_rate=10.1,
            range_rate_measured=True,
            range_rate_unc=10.1,
            range_unc=10.1,
            raw_file_uri="Example URI",
            reference_level=10.1,
            relative_carrier_power=10.1,
            relative_noise_floor=10.1,
            resolution_bandwidth=10.1,
            sat_no=32258,
            senalt=10.1,
            senlat=45.2,
            senlon=80.3,
            signal_ids=["ID1", "ID2"],
            snr=10.1,
            snrs=[1.1, 2.2],
            spectrum_analyzer_power=10.1,
            start_frequency=10.1,
            switch_point=10,
            symbol_to_noise_ratio=10.1,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            task_id="TASK-ID",
            telemetry_ids=["ID1", "ID2"],
            track_id="TRACK-ID",
            track_range=10.1,
            transaction_id="TRANSACTION-ID",
            transmit_filter_roll_off=10.1,
            transmit_filter_type="RRC",
            transponder="TRANSPONDER-A",
            uct=False,
            url="https://some-url",
            video_bandwidth=10.1,
        )
        assert rf_observation is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.rf_observation.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            type="RF",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_observation = await response.parse()
        assert rf_observation is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.rf_observation.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            type="RF",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_observation = await response.parse()
            assert rf_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_observation = await async_client.observations.rf_observation.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[RfObservationListResponse], rf_observation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_observation = await async_client.observations.rf_observation.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[RfObservationListResponse], rf_observation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.rf_observation.with_raw_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_observation = await response.parse()
        assert_matches_type(AsyncOffsetPage[RfObservationListResponse], rf_observation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.rf_observation.with_streaming_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_observation = await response.parse()
            assert_matches_type(AsyncOffsetPage[RfObservationListResponse], rf_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_observation = await async_client.observations.rf_observation.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, rf_observation, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_observation = await async_client.observations.rf_observation.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, rf_observation, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.rf_observation.with_raw_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_observation = await response.parse()
        assert_matches_type(str, rf_observation, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.rf_observation.with_streaming_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_observation = await response.parse()
            assert_matches_type(str, rf_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_observation = await async_client.observations.rf_observation.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                    "type": "RF",
                }
            ],
        )
        assert rf_observation is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.rf_observation.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                    "type": "RF",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_observation = await response.parse()
        assert rf_observation is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.rf_observation.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                    "type": "RF",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_observation = await response.parse()
            assert rf_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_observation = await async_client.observations.rf_observation.get(
            id="id",
        )
        assert_matches_type(RfObservationGetResponse, rf_observation, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_observation = await async_client.observations.rf_observation.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(RfObservationGetResponse, rf_observation, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.rf_observation.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_observation = await response.parse()
        assert_matches_type(RfObservationGetResponse, rf_observation, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.rf_observation.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_observation = await response.parse()
            assert_matches_type(RfObservationGetResponse, rf_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.observations.rf_observation.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_observation = await async_client.observations.rf_observation.queryhelp()
        assert rf_observation is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.rf_observation.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_observation = await response.parse()
        assert rf_observation is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.rf_observation.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_observation = await response.parse()
            assert rf_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_observation = await async_client.observations.rf_observation.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(RfObservationTupleResponse, rf_observation, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_observation = await async_client.observations.rf_observation.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(RfObservationTupleResponse, rf_observation, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.rf_observation.with_raw_response.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_observation = await response.parse()
        assert_matches_type(RfObservationTupleResponse, rf_observation, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.rf_observation.with_streaming_response.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_observation = await response.parse()
            assert_matches_type(RfObservationTupleResponse, rf_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_observation = await async_client.observations.rf_observation.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                    "type": "RF",
                }
            ],
        )
        assert rf_observation is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.rf_observation.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                    "type": "RF",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_observation = await response.parse()
        assert rf_observation is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.rf_observation.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                    "type": "RF",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_observation = await response.parse()
            assert rf_observation is None

        assert cast(Any, response.is_closed) is True
