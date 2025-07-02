# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.types.sensor import (
    CalibrationQueryResponse,
    CalibrationTupleResponse,
    CalibrationRetrieveResponse,
    CalibrationQueryHelpResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCalibration:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        calibration = client.sensor.calibration.create(
            classification_marking="U",
            data_mode="TEST",
            id_sensor="09f2c68c-5e24-4b72-9cc8-ba9b1efa82f0",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123Z"),
        )
        assert calibration is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        calibration = client.sensor.calibration.create(
            classification_marking="U",
            data_mode="TEST",
            id_sensor="09f2c68c-5e24-4b72-9cc8-ba9b1efa82f0",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            id="026dd511-8ba5-47d3-9909-836149f87686",
            az_ra_accel_bias=0.0123,
            az_ra_accel_sigma=0.0123,
            az_ra_bias=0.327883,
            az_ra_rate_bias=0.123,
            az_ra_rate_sigma=0.123,
            az_ra_rms=0.605333,
            az_ra_sigma=0.000381,
            cal_angle_ref="AZEL",
            cal_track_mode="INTRA_TRACK",
            cal_type="OPERATIONAL",
            confidence_noise_bias=0.001477,
            duration=14.125,
            ecr=[352815.1, -5852915.3, 3255189],
            el_dec_accel_bias=0.0123,
            el_dec_accel_sigma=0.0123,
            el_dec_bias=0.012555,
            el_dec_rate_bias=0.123,
            el_dec_rate_sigma=0.123,
            el_dec_rms=0.080505,
            el_dec_sigma=0.00265,
            end_time=parse_datetime("2018-01-14T16:00:00.123Z"),
            num_az_ra_obs=339,
            num_el_dec_obs=339,
            num_obs=341,
            num_photo_obs=77,
            num_range_obs=341,
            num_range_rate_obs=341,
            num_rcs_obs=325,
            num_time_obs=307,
            num_tracks=85,
            origin="THIRD_PARTY_DATASOURCE",
            photo_bias=0.123,
            photo_sigma=0.0123,
            range_accel_bias=0.123,
            range_accel_sigma=0.0123,
            range_bias=0.024777,
            range_rate_bias=0.105333,
            range_rate_rms=0.000227,
            range_rate_sigma=0.000321,
            range_rms=0.0123,
            range_sigma=0.042644,
            rcs_bias=0.123,
            rcs_sigma=0.0123,
            ref_targets=["xx", "yy", "zz"],
            ref_type="SLR",
            sen_type="PHASED ARRAY",
            time_bias=0.000372,
            time_bias_sigma=15.333212,
        )
        assert calibration is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.sensor.calibration.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_sensor="09f2c68c-5e24-4b72-9cc8-ba9b1efa82f0",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calibration = response.parse()
        assert calibration is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.sensor.calibration.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_sensor="09f2c68c-5e24-4b72-9cc8-ba9b1efa82f0",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calibration = response.parse()
            assert calibration is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        calibration = client.sensor.calibration.retrieve(
            id="id",
        )
        assert_matches_type(CalibrationRetrieveResponse, calibration, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        calibration = client.sensor.calibration.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(CalibrationRetrieveResponse, calibration, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.sensor.calibration.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calibration = response.parse()
        assert_matches_type(CalibrationRetrieveResponse, calibration, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.sensor.calibration.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calibration = response.parse()
            assert_matches_type(CalibrationRetrieveResponse, calibration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sensor.calibration.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        calibration = client.sensor.calibration.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, calibration, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        calibration = client.sensor.calibration.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, calibration, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.sensor.calibration.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calibration = response.parse()
        assert_matches_type(str, calibration, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.sensor.calibration.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calibration = response.parse()
            assert_matches_type(str, calibration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        calibration = client.sensor.calibration.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sensor": "09f2c68c-5e24-4b72-9cc8-ba9b1efa82f0",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123Z"),
                }
            ],
        )
        assert calibration is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.sensor.calibration.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sensor": "09f2c68c-5e24-4b72-9cc8-ba9b1efa82f0",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calibration = response.parse()
        assert calibration is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.sensor.calibration.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sensor": "09f2c68c-5e24-4b72-9cc8-ba9b1efa82f0",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calibration = response.parse()
            assert calibration is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query(self, client: Unifieddatalibrary) -> None:
        calibration = client.sensor.calibration.query(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(CalibrationQueryResponse, calibration, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: Unifieddatalibrary) -> None:
        calibration = client.sensor.calibration.query(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(CalibrationQueryResponse, calibration, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: Unifieddatalibrary) -> None:
        response = client.sensor.calibration.with_raw_response.query(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calibration = response.parse()
        assert_matches_type(CalibrationQueryResponse, calibration, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: Unifieddatalibrary) -> None:
        with client.sensor.calibration.with_streaming_response.query(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calibration = response.parse()
            assert_matches_type(CalibrationQueryResponse, calibration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        calibration = client.sensor.calibration.query_help()
        assert_matches_type(CalibrationQueryHelpResponse, calibration, path=["response"])

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.sensor.calibration.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calibration = response.parse()
        assert_matches_type(CalibrationQueryHelpResponse, calibration, path=["response"])

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.sensor.calibration.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calibration = response.parse()
            assert_matches_type(CalibrationQueryHelpResponse, calibration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        calibration = client.sensor.calibration.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(CalibrationTupleResponse, calibration, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        calibration = client.sensor.calibration.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(CalibrationTupleResponse, calibration, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.sensor.calibration.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calibration = response.parse()
        assert_matches_type(CalibrationTupleResponse, calibration, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.sensor.calibration.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calibration = response.parse()
            assert_matches_type(CalibrationTupleResponse, calibration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        calibration = client.sensor.calibration.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sensor": "09f2c68c-5e24-4b72-9cc8-ba9b1efa82f0",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123Z"),
                }
            ],
        )
        assert calibration is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.sensor.calibration.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sensor": "09f2c68c-5e24-4b72-9cc8-ba9b1efa82f0",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calibration = response.parse()
        assert calibration is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.sensor.calibration.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sensor": "09f2c68c-5e24-4b72-9cc8-ba9b1efa82f0",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calibration = response.parse()
            assert calibration is None

        assert cast(Any, response.is_closed) is True


class TestAsyncCalibration:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        calibration = await async_client.sensor.calibration.create(
            classification_marking="U",
            data_mode="TEST",
            id_sensor="09f2c68c-5e24-4b72-9cc8-ba9b1efa82f0",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123Z"),
        )
        assert calibration is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        calibration = await async_client.sensor.calibration.create(
            classification_marking="U",
            data_mode="TEST",
            id_sensor="09f2c68c-5e24-4b72-9cc8-ba9b1efa82f0",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            id="026dd511-8ba5-47d3-9909-836149f87686",
            az_ra_accel_bias=0.0123,
            az_ra_accel_sigma=0.0123,
            az_ra_bias=0.327883,
            az_ra_rate_bias=0.123,
            az_ra_rate_sigma=0.123,
            az_ra_rms=0.605333,
            az_ra_sigma=0.000381,
            cal_angle_ref="AZEL",
            cal_track_mode="INTRA_TRACK",
            cal_type="OPERATIONAL",
            confidence_noise_bias=0.001477,
            duration=14.125,
            ecr=[352815.1, -5852915.3, 3255189],
            el_dec_accel_bias=0.0123,
            el_dec_accel_sigma=0.0123,
            el_dec_bias=0.012555,
            el_dec_rate_bias=0.123,
            el_dec_rate_sigma=0.123,
            el_dec_rms=0.080505,
            el_dec_sigma=0.00265,
            end_time=parse_datetime("2018-01-14T16:00:00.123Z"),
            num_az_ra_obs=339,
            num_el_dec_obs=339,
            num_obs=341,
            num_photo_obs=77,
            num_range_obs=341,
            num_range_rate_obs=341,
            num_rcs_obs=325,
            num_time_obs=307,
            num_tracks=85,
            origin="THIRD_PARTY_DATASOURCE",
            photo_bias=0.123,
            photo_sigma=0.0123,
            range_accel_bias=0.123,
            range_accel_sigma=0.0123,
            range_bias=0.024777,
            range_rate_bias=0.105333,
            range_rate_rms=0.000227,
            range_rate_sigma=0.000321,
            range_rms=0.0123,
            range_sigma=0.042644,
            rcs_bias=0.123,
            rcs_sigma=0.0123,
            ref_targets=["xx", "yy", "zz"],
            ref_type="SLR",
            sen_type="PHASED ARRAY",
            time_bias=0.000372,
            time_bias_sigma=15.333212,
        )
        assert calibration is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor.calibration.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_sensor="09f2c68c-5e24-4b72-9cc8-ba9b1efa82f0",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calibration = await response.parse()
        assert calibration is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor.calibration.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_sensor="09f2c68c-5e24-4b72-9cc8-ba9b1efa82f0",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calibration = await response.parse()
            assert calibration is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        calibration = await async_client.sensor.calibration.retrieve(
            id="id",
        )
        assert_matches_type(CalibrationRetrieveResponse, calibration, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        calibration = await async_client.sensor.calibration.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(CalibrationRetrieveResponse, calibration, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor.calibration.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calibration = await response.parse()
        assert_matches_type(CalibrationRetrieveResponse, calibration, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor.calibration.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calibration = await response.parse()
            assert_matches_type(CalibrationRetrieveResponse, calibration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sensor.calibration.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        calibration = await async_client.sensor.calibration.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, calibration, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        calibration = await async_client.sensor.calibration.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, calibration, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor.calibration.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calibration = await response.parse()
        assert_matches_type(str, calibration, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor.calibration.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calibration = await response.parse()
            assert_matches_type(str, calibration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        calibration = await async_client.sensor.calibration.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sensor": "09f2c68c-5e24-4b72-9cc8-ba9b1efa82f0",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123Z"),
                }
            ],
        )
        assert calibration is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor.calibration.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sensor": "09f2c68c-5e24-4b72-9cc8-ba9b1efa82f0",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calibration = await response.parse()
        assert calibration is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor.calibration.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sensor": "09f2c68c-5e24-4b72-9cc8-ba9b1efa82f0",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calibration = await response.parse()
            assert calibration is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        calibration = await async_client.sensor.calibration.query(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(CalibrationQueryResponse, calibration, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        calibration = await async_client.sensor.calibration.query(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(CalibrationQueryResponse, calibration, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor.calibration.with_raw_response.query(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calibration = await response.parse()
        assert_matches_type(CalibrationQueryResponse, calibration, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor.calibration.with_streaming_response.query(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calibration = await response.parse()
            assert_matches_type(CalibrationQueryResponse, calibration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        calibration = await async_client.sensor.calibration.query_help()
        assert_matches_type(CalibrationQueryHelpResponse, calibration, path=["response"])

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor.calibration.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calibration = await response.parse()
        assert_matches_type(CalibrationQueryHelpResponse, calibration, path=["response"])

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor.calibration.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calibration = await response.parse()
            assert_matches_type(CalibrationQueryHelpResponse, calibration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        calibration = await async_client.sensor.calibration.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(CalibrationTupleResponse, calibration, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        calibration = await async_client.sensor.calibration.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(CalibrationTupleResponse, calibration, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor.calibration.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calibration = await response.parse()
        assert_matches_type(CalibrationTupleResponse, calibration, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor.calibration.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calibration = await response.parse()
            assert_matches_type(CalibrationTupleResponse, calibration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        calibration = await async_client.sensor.calibration.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sensor": "09f2c68c-5e24-4b72-9cc8-ba9b1efa82f0",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123Z"),
                }
            ],
        )
        assert calibration is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor.calibration.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sensor": "09f2c68c-5e24-4b72-9cc8-ba9b1efa82f0",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calibration = await response.parse()
        assert calibration is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor.calibration.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sensor": "09f2c68c-5e24-4b72-9cc8-ba9b1efa82f0",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calibration = await response.parse()
            assert calibration is None

        assert cast(Any, response.is_closed) is True
